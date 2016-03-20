import numpy as np
if 1:
    posz,trans1=genfromtxt(trans_file,unpack=1)
    zcentroid=integral(trans1*posz,posz)/integral(trans1,posz)
    
    mmin,dm=np.genfromtxt(fn,unpack=1)
    likely=np.genfromtxt(fn1,unpack=1)
    mmax=mmin+dm
    
    focc=np.zeros_like(mmax)
    focc_up=np.zeros_like(mmax)
    focc_low=np.zeros_like(mmax)
    focc_up1=np.zeros_like(mmax)
    focc_low1=np.zeros_like(mmax)

    
    mmed=np.zeros_like(mmax)
    m_up=np.zeros_like(mmax)
    m_low=np.zeros_like(mmax)
    m_up1=np.zeros_like(mmax)
    m_low1=np.zeros_like(mmax)


    
    for count1 in range(len(mmax)):
        
        count=0
        
        frac=np.zeros(nx*ny*nz)
        mmedian=np.zeros(nx*ny*nz)
        for i,j,k in itertools.product(range(nx),range(ny),range(nz)):
            
            
            m1=mass[index[count]];z1=z[index[count]]
            m1=np.log10(m1)
            wmin=m1>mmin[count1]; wmax=m1<mmax[count1]
            
            wm=wmin*wmax
            mm=m1[wm]
            zm=z1[wm]
            if len(mm)==0: continue
            #print np.log10(Nlae_mean/(1.0*len(mm)))
            prob=np.random.rand(len(zm))
            zcenter=(z1.max()+z1.min())/2.0 - zcentroid 
            posz1=posz+zcenter
            trans_func = interp1d(posz1, trans1, kind='linear',bounds_error=False,fill_value=0)
            pz=trans_func(zm)
            wz=pz>prob
            zapp=zm[wz]
            frac[count]=np.log10(Nlae_mean/(1.0*len(zapp)))
            count=count+1
        if np.sum(frac)==0: continue 
        focc[count1]=np.percentile(frac,50)
        focc_low[count1]=np.percentile(frac,16)
        focc_up[count1]=np.percentile(frac,84)
        focc_low1[count1]=np.percentile(frac,2.5)
        focc_up1[count1]=np.percentile(frac,97.5)
        m1=np.log10(mass)
        wmin=m1>mmin[count1]; wmax=m1<mmax[count1]
        wm=wmin*wmax
        mm=m1[wm]
        mmed[count1]=np.percentile(mm,50)
        m_up[count1]=np.percentile(mm,84)
        m_low[count1]=np.percentile(mm,16)
        m_up1[count1]=np.percentile(mm,97.5)
        m_low1[count1]=np.percentile(mm,2.5)

        
    np.savetxt('../output/focc'+sufix+'.txt',np.transpose([mmin,mmax,focc,focc_low,focc_up,focc_low1,focc_up1,mmed,m_low,m_up,m_low1,m_up1,likely]))
