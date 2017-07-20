import numpy as np
import os.path
import glob
from pprint import pprint
import time

sort_by_clusters = False

clusterdist = np.array([0.8])
clusterdist = np.array([0.8,1.41,1.61,2.1, 2.41])
clusterdist = np.array([0.8,1.4,1.6,2.1,2.4,2.8,2.9,3.2,3.5,3.7])

# atomlist = [31,32,33,34,35,36]
# atomlist = [51,52,53,54,55,56]
atomlist = [41,42,43,44,45,46,47,48,49,50]
atomlist = [31,32,33,34,35,36,37,38,39,40]
atomlist = [51,52,53,54,55,56,57,58,59,60]
atomlist = [31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60]
print "atomlist ", atomlist

target = open("Dij fullslab auto complet.dat", 'w')

# posaux    = np.zeros((len(atomlist),len(atompos),11), dtype=np.float32)
max_num_neighb=1000
# posaux = np.zeros((len(atomlist),max_num_neighb,11), dtype=np.float32)
mod_R      = np.zeros((len(atomlist),max_num_neighb,1), dtype=np.float32)
# atomj_indx = np.zeros((len(atomlist),max_num_neighb,1), dtype=np.float32)
Rij = np.zeros((len(atomlist),max_num_neighb,3), dtype=np.float32)
Dij = np.zeros((len(atomlist),max_num_neighb,3), dtype=np.float32)
Jij = np.zeros((len(atomlist),max_num_neighb,3), dtype=np.float32)
atomij_indx = np.zeros((len(atomlist),max_num_neighb,2), dtype=np.float32)

for atomi, atomi_listitem in enumerate(atomlist):
   # print "Atom", atomi_listitem, "Rx              Ry              Rz              Dx              Dy              Dz              Jx              Jy              Jz      "
   target.write( "Atom "+ str(atomi_listitem)+ " Rx              Ry              Rz              Dx              Dy              Dz              Jx              Jy              Jz      \n" )
   neighb_counter = 0
   for atomj, atomj_listitem in enumerate(atomlist):
      for k, component  in enumerate(["x","y","z"]):
         # allfilenames=glob.glob('./magnetization_'+component+'/*_'+str(atomi_listitem)+'_*/SYSTEM*/Jij.atom*')
         if atomi_listitem <= atomj_listitem :
            allfilenames=glob.glob('./magnetization_'+component+'/*_'+str(atomi_listitem)+'_'+str(atomj_listitem)+'/SYSTEM*/Jij.atom*')
         else:
            allfilenames=glob.glob('./magnetization_'+component+'/*_'+str(atomj_listitem)+'_'+str(atomi_listitem)+'/SYSTEM*/Jij.atom*')

         if k==0:
            atomj = []
         
         file = open(allfilenames[0])
         lines = file.readlines()
         
         # print file
         # time.sleep(1)
         
         if k == 0 :
            # Coordinates of the vectors
            RR = []
            Rx = []
            Ry = []
            Rz = []
            Dx = []
            Jx = []
            jindx = []
            # Read data columns into the respective arrays
            for line in lines[0:1000]:
               if not line.startswith("#"):
                  data_str = line.split()
                  RR.append(float(data_str[0]))
                  Jx.append(float(data_str[1]))
                  Dx.append(float(data_str[2]))
                  Rx.append(float(data_str[5]))
                  Ry.append(float(data_str[6]))
                  Rz.append(float(data_str[7]))
                  jindx.append(float(data_str[8]))

         # print Rx
         # print Ry
         # print Rz
         # exit()

         if k == 1 :
            Dy = []
            Jy = []
            # Read data columns into the respective arrays
            for line in lines[0:1000]:
               if not line.startswith("#"):
                  data_str = line.split()
                  Jy.append(float(data_str[1]))
                  Dy.append(float(data_str[2]))

         if k == 2 :
            Dz = []
            Jz = []
            # Read data columns into the respective arrays
            for line in lines[0:1000]:
               if not line.startswith("#"):
                  data_str = line.split()
                  Jz.append(float(data_str[1]))
                  Dz.append(float(data_str[2]))

      for i, itemRR in enumerate(RR):
         mod_R[atomi,neighb_counter,0] = RR[i]
         Jij[atomi,neighb_counter,:] = [ Jx[i], Jy[i], Jz[i] ]
         atomij_indx[atomi,neighb_counter,:] = [ atomi_listitem-31, atomj_listitem-31 ]

         if atomi_listitem <= atomj_listitem :
            Rij[atomi,neighb_counter,:] = [ Rx[i], Ry[i], Rz[i] ]
            Dij[atomi,neighb_counter,:] = [ Dx[i], Dy[i], Dz[i] ]
         else :
            Rij[atomi,neighb_counter,:] = [ -Rx[i], -Ry[i], -Rz[i] ]
            Dij[atomi,neighb_counter,:] = [ -Dx[i], -Dy[i], -Dz[i] ]

         # print "%16.8e"*3 % tuple(Rij[atomi,neighb_counter,:])+"%16.8e"*3 % tuple(Dij[atomi,neighb_counter,:])+"%16.8e"*3 % tuple(Jij[atomi,neighb_counter,:])
         target.write( "%16.8f"*3 % tuple(Rij[atomi,neighb_counter,:])+"%16.8e"*3 % tuple(Dij[atomi,neighb_counter,:])+"%16.8e"*3 % tuple(Jij[atomi,neighb_counter,:]) + "%3d"*2 % tuple(atomij_indx[atomi,neighb_counter,:]) + "\n" )
         
         neighb_counter += 1
   print "Atomi", atomi_listitem, "n. neighbours:", neighb_counter 






