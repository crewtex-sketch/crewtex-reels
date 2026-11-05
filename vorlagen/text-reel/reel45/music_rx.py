import sys
exec(open(__file__.replace('music_rx.py','music_base.py')).read())
# Drift-Phonk: Cowbell-Riff, verzerrter 808, harte Drums. argv[5]=='fx' -> nur Soundeffekte
which=sys.argv[1]; CUTS7=[3.0,8.6,13.0,17.4]; END7=17.4; FXONLY=len(sys.argv)>5 and sys.argv[5]=='fx'
BAR=4*B; S16=B/4
if which=='r6':
    ROOTS=[31,31,27,29]            # G, G, Eb, F
    RIFF=[79,0,82,79,0,77,79,0,74,0,77,0,79,82,84,82]
    RIFF2=[79,0,82,79,0,77,79,0,86,0,84,0,82,0,79,77]
    CUTS=[3.0,9.0,12.9,17.2]; END=17.2
elif which=='r7':
    ROOTS=[26,26,22,24]            # D, D, Bb, C
    RIFF=[74,0,77,74,0,72,74,0,69,0,72,0,74,77,79,77]
    RIFF2=[74,0,77,74,0,72,74,0,81,0,79,0,77,0,74,72]
    CUTS=CUTS7; END=END7
elif which=='r4':
    ROOTS=[33,33,29,31]            # A, A, F, G
    RIFF=[81,0,84,81,0,79,81,0,76,0,79,0,81,84,86,84]
    RIFF2=[81,0,84,81,0,79,81,0,88,0,86,0,84,0,81,79]
    CUTS=[3.0,7.0,11.0,15.0,18.6]; END=18.6
else:
    ROOTS=[28,28,24,26]            # E, E, C, D
    RIFF=[76,0,79,76,0,74,76,0,71,0,74,0,76,79,81,79]
    RIFF2=[76,0,79,76,0,74,76,0,83,0,81,0,79,0,76,74]
    CUTS=[3.0,13.6,17.4]; END=17.4
def sq(f,t): return np.sign(np.sin(2*np.pi*f*t))
def cowbell(n,d=.22):
    f=mid(n); t=T(d)
    s=sq(f,t)*.6+sq(f*1.48,t)*.4
    s=hp(lp(s,f*3.2),f*.7)
    return s*np.exp(-t*14)*np.minimum(1,t/.001)*.55
def b808(n,d):
    t=T(d); f=mid(n)*(1+.6*np.exp(-t*40))
    s=np.sin(2*np.pi*np.cumsum(f)/SR)
    s=np.tanh(s*4.5)*.7
    e=np.exp(-t*.9); rl=min(len(t)-1,int(.02*SR)); e[-rl:]*=np.linspace(1,0,rl)
    return s*e
def pkick():
    t=T(.3); f=50+230*np.exp(-t*55); s=np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-t*12)
    s[:150]+=rng.standard_normal(150)*np.linspace(.9,0,150); return np.tanh(s*2.6)
def psnare():
    t=T(.3); n=hp(rng.standard_normal(len(t)),1500)*np.exp(-t*18)
    body=np.sin(2*np.pi*np.cumsum(200+90*np.exp(-t*45))/SR)*np.exp(-t*20)
    return np.tanh((n*.7+body*.6)*1.8)*.8
def phat(g=1.0):
    t=T(.03); return hp(rng.standard_normal(len(t)),9000)*np.exp(-t*130)*.3*g
def bar(t0,blen,i,intro=False):
    riff=RIFF if i%2==0 else RIFF2
    for k,n in enumerate(riff):
        tt=t0+k*S16
        if k*S16>=blen: break
        if n: add('lead',cowbell(n),tt,.75 if not intro else .6,(-.2 if k%2 else .2))
    if intro: return
    for p in (0,6,10):
        if p*S16<blen: add('drums',pkick(),t0+p*S16,1.0); kicks.append(t0+p*S16)
    for p in (4,12):
        if p*S16<blen: add('drums',psnare(),t0+p*S16,.85); add('drums',clap(),t0+p*S16,.35)
    for k in range(16):
        if k*S16>=blen: break
        if i%2==1 and k>=14:
            for r in range(3): add('drums',phat(.8),t0+k*S16+r*S16/3,1,.25)
        else: add('drums',phat(1 if k%2==0 else .55),t0+k*S16,1,.25 if k%4 else -.2)
    r=ROOTS[i%4]
    for p,l in ((0,6),(6,4),(10,6)):
        if p*S16<blen: add('bass',b808(r,min(l*S16,blen-p*S16)),t0+p*S16,.8)
# Intro: Riff gefiltert, Riser, Impact auf 3.0
t0=0.25
while t0<2.9: bar(t0,min(BAR,2.9-t0),0,intro=True); t0+=BAR
for k in range(8): add('drums',phat(.5),1.7+k*S16,1,.2)
for k in range(4): add('drums',psnare(),2.45+k*S16*.75,.25+.15*k)
add('fx',lp(noise_rise(1.3),6000),1.7,.7)
# Hauptteil
t0=3.0; i=0
while t0<END-0.01: bar(t0,min(BAR,END-t0),i); i+=1; t0+=BAR
for c in CUTS: add('fx',whoosh(.5),c-.32,.85)
add('fx',impact(),3.0,1.0); add('fx',impact(),END,.9)
if which=='r6':
    for k in range(12): add('fx',tick(),3.15+k*.42,.7,.3*(1 if k%2 else -1))
    add('fx',impact(),7.75,.8)
    for k in range(8): add('fx',tick(),10.05+k*.2,.5,.3*(1 if k%2 else -1))
    add('fx',ding(88),12.5,.6)
    for k in range(6): add('fx',thud(),13.25+k*.15+.3,.6,.3*((k%3)-1))
    for k in range(4): add('fx',tick(),19.6+k*.2,.8)
    add('fx',ding(93),20.45,.6)
elif which=='r7':
    exec(open(__file__.replace('music_rx.py','fx_r7.py')).read())
elif which=='r4':
    for t in (4.2,5.0,5.8): add('fx',tick(),t,1.0)
    add('fx',ding(88),5.9,.8)
    add('fx',thud(),9.9,.8); add('fx',ding(93),10.0,.5)
    for k in range(10): add('fx',tick(),12.1+k*.22,.5,.3*(1 if k%2 else -1))
    for k in range(6): add('fx',thud(),15.35+k*.16+.3,.6,.3*((k%3)-1))
    add('fx',ding(93),16.9,.6)
else:
    for t in (3.4,4.6,5.8,7.0,8.2,9.4,10.6,11.8): add('fx',tick(),t,.75); add('fx',whoosh(.35),t+.5,.45,.3)
    for t in (15.4,16.0,16.6): add('fx',ding(93),t,.7,.2)
    add('fx',thud(),14.65,.6)
# Outro: Riff ohne Drums, 808 lang
t0=END
while t0<DUR-.4: bar(t0,min(BAR,DUR-.4-t0),0,intro=True); t0+=BAR
add('bass',b808(ROOTS[0],DUR-END),END,.7)
sc=np.ones(N)
for k in kicks:
    a=int(k*SR); n=int(.15*SR); j=min(N,a+n); xx=np.arange(j-a)/SR
    sc[a:j]=np.minimum(sc[a:j],1-.35*np.exp(-xx*16))
if FXONLY:
    mixL=bus['fx']
else:
    ig=np.ones(N); _m=int(3*SR); x=np.linspace(0,1,_m); ig[:_m]=.35+.55*x**2
    lead=bus['lead'].copy(); lead[:, :_m]*=ig[:_m]
    mixL=bus['drums']*.95+bus['bass']*.95+lead*sc+bus['fx']*.7
fade=np.ones(N); fs=int((DUR-1.2)*SR); fade[fs:]=np.linspace(1,0,N-fs); fade[:int(.03*SR)]=np.linspace(0,1,int(.03*SR))
mixL=mixL*fade
mm=np.abs(mixL).max(); out=np.tanh(mixL/mm*(1.2 if FXONLY else 1.7))*.92
stt=np.empty(N*2); stt[0::2]=out[0]; stt[1::2]=out[1]
w=wave.open(sys.argv[4],'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
w.writeframes((stt*32767).astype(np.int16).tobytes()); w.close(); print('ok',which,FXONLY)
