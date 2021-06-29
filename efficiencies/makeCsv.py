from V32_stats_Lxy1300_tkPt500MeV_lepPt400MeV_points import m_ctau_eff_time_s as points_B  
from V32_stats_Lxy1300_tkPt500MeV_lepPt400MeV_Bc_points import m_ctau_eff_time_s as points_Bc


fout = open('request.csv', 'w')
fout.write('dataset,fragment,events,generator,time per event,filter efficiency\n')

all_points = [(m,ctau,eff,time,'B') for m,ctau,eff,time in points_B] + [(m,ctau,eff,time,'Bc') for m,ctau,eff,time in points_Bc]

for m,ctau,eff,time,spc in all_points:
  if ctau!=0.01:
    name = '{}ToNMuX_NToEMuPi_SoftQCD_b_mN{:.1f}_ctau{:.1f}mm'.format(spc,m,ctau)
  else:
    name = '{}ToNMuX_NToEMuPi_SoftQCD_b_mN{:.1f}_ctau{:.2f}mm'.format(spc,m,ctau)

  ds = name + '_TuneCP5_13TeV-pythia8'
  path = 'genFragments/Generator/Pythia/BHNL/'
  fragment = path + name + '_TuneCP5_13TeV_pythia8-evtgen' + '_cfi.py' 
  events = 100000
  generator = 'pythia8'
  timeperevent = '{:.2e}'.format(time*eff)
  filterefficiency = '{:.2e}'.format(eff)

  fout.write('{dataset},{fragment},{events},{generator},{timeperevent},{filterefficiency}\n'.format(
                dataset=ds, fragment=fragment, events=events, generator=generator,
                timeperevent=timeperevent, filterefficiency=filterefficiency))
  
fout.close() 
