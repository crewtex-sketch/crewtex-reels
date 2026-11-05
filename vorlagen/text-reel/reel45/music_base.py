import numpy as np, wave
import sys
SR=44100; DUR=float(sys.argv[2]); N=int(SR*DUR); BPM=float(sys.argv[3]); B=60/BPM; E8=B/2
rng=np.random.default_rng(3)
bus={k:np.zeros((2,N)) for k in ['drums','bass','lead','pad','fx','intro']}
def T(d): return np.arange(int(SR*d))/SR
def add(b,sig,start,g=1.0,pan=0.0):
    i=int(round(start*SR)); 
    if i>=N: return
    j=min(N,i+len(sig)); s=sig[:j-i]*g
    bus[b][0,i:j]+=s*(1-max(0,pan)); bus[b][1,i:j]+=s*(1+min(0,pan))
def lp(x,c):
    a=np.exp(-2*np.pi*c/SR); y=np.empty_like(x); z=0.0
    for i in range(len(x)): z=(1-a)*x[i]+a*z; y[i]=z
    return y
def hp(x,c): return x-lp(x,c)
def mid(n): return 440*2**((n-69)/12)
def saw(f,d,h=14,det=0.0):
    t=T(d); s=np.zeros_like(t)
    for k in range(1,h+1):
        if f*k>16000: break
        s+=np.sin(2*np.pi*f*(1+det)*k*t)/k
    return s*0.55
def adsr(n,a=.004,d=.15,s=.5,r=.05):
    t=np.arange(n)/SR; e=np.where(t<a,t/a,s+(1-s)*np.exp(-(t-a)/d))
    rl=int(r*SR); 
    if rl<n: e[-rl:]*=np.linspace(1,0,rl)
    return e
# ---- instruments
def kick():
    t=T(.5); f=45+150*np.exp(-t*35); s=np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-t*6.5)
    s[:200]+=rng.standard_normal(200)*np.linspace(.5,0,200); return np.tanh(s*1.6)
def clap():
    t=T(.3); n=hp(rng.standard_normal(len(t)),1200)
    e=np.zeros_like(t)
    for o in (0,.009,.018): e+=np.exp(-np.clip(t-o,0,None)*120)*(t>=o)
    e+=0.5*np.exp(-t*14); snare=np.sin(2*np.pi*190*t)*np.exp(-t*30)*.6
    return (n*e*.45+snare)
def hat(o=False):
    t=T(.2 if o else .05); n=hp(rng.standard_normal(len(t)),7500); return n*np.exp(-t*(16 if o else 85))*.3
def bell(n,d=.9):
    f=mid(n); t=T(d)
    s=(np.sin(2*np.pi*f*t)+.4*np.sin(2*np.pi*f*2*t)*np.exp(-t*6)+.25*np.sin(2*np.pi*f*3.01*t)*np.exp(-t*9))
    return s*np.exp(-t*4.5)*.35
def soft(n,d=.9):
    f=mid(n); t=T(d)
    s=np.sin(2*np.pi*f*t)+.18*np.sin(2*np.pi*f*2*t)*np.exp(-t*10)
    a=np.minimum(1,t/.012)
    return lp(s*a*np.exp(-t*5.5),2200)*.42
def lead(n,d):
    f=mid(n); s=sum(saw(f,d+.05,14,dt) for dt in (-.006,0,.006))/3
    t=T(d+.05); cut=1500+5000*np.exp(-t*9)
    s=lp(s,2600)*.8+hp(s,3000)*.25*np.exp(-t*8)
    return s*adsr(len(s),.003,.18,.45,.04)
def bass(n,d):
    f=mid(n); t=T(d); sub=np.sin(2*np.pi*f*t)
    grit=lp(saw(f,d,8),500)
    return (sub*.9+grit*.5)*adsr(len(t),.004,.25,.7,.03)
def pad(ns,d):
    out=None
    for n in ns:
        s=lp(saw(mid(n),d,10,.004)+saw(mid(n),d,10,-.004),1100)
        out=s if out is None else out+s
    t=T(d); return out*np.minimum(1,t/.25)*.07
def noise_rise(d):
    t=T(d); n=rng.standard_normal(len(t)); x=t/d
    return (hp(n,800)*x**2.2*.45)
def impact():
    t=T(1.8); sub=np.sin(2*np.pi*np.cumsum(40+60*np.exp(-t*7))/SR)*np.exp(-t*2)
    n=lp(rng.standard_normal(len(t)),1500)*np.exp(-t*5)
    return np.tanh((sub+n*.5)*1.4)
def rev_cym(d):
    t=T(d); n=hp(rng.standard_normal(len(t)),4000); return n*(t/d)**3*.35
kicks=[]
def tick():
    t=T(.04); return hp(rng.standard_normal(len(t)),4000)*np.exp(-t*120)*.5
def thud():
    t=T(.35); s=np.sin(2*np.pi*np.cumsum(60+70*np.exp(-t*30))/SR)*np.exp(-t*12)
    return np.tanh((s+lp(rng.standard_normal(len(t)),900)*np.exp(-t*25)*.6)*1.4)
def whoosh(d=.45):
    t=T(d); n=lp(hp(rng.standard_normal(len(t)),700),6000); x=t/d
    return n*np.sin(np.pi*x)**1.5*.6
def ding(n=93):
    f=mid(n); t=T(.7); return (np.sin(2*np.pi*f*t)+.3*np.sin(2*np.pi*f*2.76*t)*np.exp(-t*8))*np.exp(-t*4.5)*.3
