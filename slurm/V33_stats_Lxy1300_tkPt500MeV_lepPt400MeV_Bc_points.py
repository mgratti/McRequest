from python.common  import Point,Config,getCtauEff

# List of points to be generated
#   - N.B.: mass must be a float


m_ctau_eff_time_s = [


(2.0,  10000.0, 1.87e-02, 29.72, 591.7),
#(2.0,   1000.0, 1.01e-01, 32.98, 598.9),
(2.0,    100.0, 1.88e-01, 45.55, 602.2),
(2.0,     10.0, 1.92e-01, 45.09, 601.6),
(3.0,   1000.0, 8.52e-02, 46.54, 608.5),
(3.0,    100.0, 1.53e-01, 45.83, 609.0),
(3.0,     10.0, 1.54e-01, 42.63, 609.0),
(3.0,      1.0, 1.54e-01, 46.37, 609.0),
(4.5,    100.0, 3.40e-02, 39.28, 630.1),
(4.5,     10.0, 3.49e-02, 30.68, 630.1),
(4.5,      1.0, 3.47e-02, 31.01, 630.6),
(4.5,      0.1, 3.47e-02, 29.74, 631.5),
(5.5,     10.0, 1.22e-03, 80.61, 681.0),
(5.5,      1.0, 1.22e-03, 82.08, 681.7),
(5.5,      0.1, 1.23e-03, 80.95, 681.6),
(5.5,     0.01, 1.19e-03, 77.47, 687.0),
# obtained with low stats
#(2.0,  10000.0, 1.59e-02, 38.74, 585.7),
#(2.0,   1000.0, 8.98e-02, 43.25, 635.7),
#(2.0,    100.0, 2.03e-01, 49.60, 658.3),
#(2.0,     10.0, 2.09e-01, 49.61, 664.5),
#(3.0,   1000.0, 9.84e-02, 44.82, 624.1),
#(3.0,    100.0, 1.59e-01, 48.49, 624.7),
#(3.0,     10.0, 1.61e-01, 48.49, 621.6),
#(3.0,      1.0, 1.61e-01, 48.49, 628.7),
#(4.5,    100.0, 4.07e-02, 46.75, 613.7),
#(4.5,     10.0, 4.08e-02, 45.29, 616.5),
#(4.5,      1.0, 4.08e-02, 48.66, 617.5),
#(4.5,      0.1, 4.08e-02, 48.72, 614.1),
#(5.5,     10.0, 9.69e-04, 149.88, 687.9),
#(5.5,      1.0, 9.69e-04, 150.07, 685.7),
#(5.5,      0.1, 9.66e-04, 152.61, 703.2),
#(5.5,     0.01, 9.99e-04, 62.53, 693.9),


## previous tune
#(2.0,  10000.00, 1.87e-02, 18),
#(2.0,   1000.00, 1.02e-01, 20),
#(2.0,    100.00, 1.86e-01, 15),
#(2.0,     10.00, 1.83e-01, 15),
#(3.0,   1000.00, 8.48e-02, 15),
#(3.0,    100.00, 1.57e-01, 16),
#(3.0,     10.00, 1.59e-01, 22),
#(3.0,      1.00, 1.59e-01, 22),
#(4.5,    100.00, 3.60e-02, 19),
#(4.5,     10.00, 3.64e-02, 20),
#(4.5,      1.00, 3.64e-02, 19),
#(4.5,      0.10, 3.64e-02, 19),
#(5.5,     10.00, 1.31e-03, 48),
#(5.5,      1.00, 1.31e-03, 51),
#(5.5,      0.10, 1.38e-03, 50),
#(5.5,      0.01, 1.35e-03, 43),


]

points = []
for m,ctau,eff,time,size in m_ctau_eff_time_s:
  p   = Point(mass=m,ctau=ctau,vv=None,ismaj=True)
  cfg = Config(nevtseff=5000,muoneff=eff,displeff=1.0,timeevt=time,timejob=12,contingency=3)
  p.setConfig(cfg)
  points.append(p)

  # 

  #print('mass={:.1f} vv={:.1e} before={:.1e}, after={:.1e}'.format(p.mass,p.vv,displEff[m][vv],getCtauEff(p.ctau*4.,1000.))) # 4 is the assumed beta*gamma factor...
  #cfg.stamp()
  







