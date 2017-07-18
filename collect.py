import numpy as np
import os.path
import glob
from pprint import pprint

sort_by_clusters = False

clusterdist = np.array([0.8])
clusterdist = np.array([0.8,1.41,1.61,2.1, 2.41])
clusterdist = np.array([0.8,1.4,1.6,2.1,2.4,2.8,2.9,3.2,3.5,3.7])

# atomlist = [31,32,33,34,35,36]
# atomlist = [51,52,53,54,55,56]
atomlist = [51,52,53,54,55,56,57,58,59,60]
atomlist = [41,42,43,44,45,46,47,48,49,50]
atomlist = [31,32,33,34,35,36,37,38,39,40]
atomlist = [31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60]
print "atomlist ", atomlist

target = open("Dij fullslab auto complet.dat", 'w')

#This is a array of vectors that correspond to the n.n sites
atompos = [
 #Cluster  1
     [ 0.90000000,  0.00000000,  0.00000000],
     [ 0.40000000,  0.70710678,  0.00000000],
     [-0.40000000,  0.70710678,  0.00000000],
     [-0.80000000,  0.00000000,  0.00000000],
     [-0.40000000, -0.70710678,  0.00000000],
     [ 0.40000000, -0.70710678,  0.00000000],
 #Cluster  2
     [ 1.20000000,  0.70710678,  0.00000000],
     [ 0.00000000,  1.41421356,  0.00000000],
     [-1.20000000,  0.70710678,  0.00000000],
     [-1.20000000, -0.70710678,  0.00000000],
     [ 0.00000000, -1.41421356,  0.00000000],
     [ 1.20000000, -0.70710678,  0.00000000],
 #Cluster  3
     [ 1.60000000,  0.00000000,  0.00000000],
     [ 0.80000000,  1.41421356,  0.00000000],
     [-0.80000000,  1.41421356,  0.00000000],
     [-1.60000000,  0.00000000,  0.00000000],
     [-0.80000000, -1.41421356,  0.00000000],
     [ 0.80000000, -1.41421356,  0.00000000],
 #Cluster  4
     [ 2.00000000,  0.70710678,  0.00000000],
     [ 1.60000000,  1.41421356,  0.00000000],
     [ 0.40000000,  2.12132034,  0.00000000],
     [-0.40000000,  2.12132034,  0.00000000],
     [-1.60000000,  1.41421356,  0.00000000],
     [-2.00000000,  0.70710678,  0.00000000],
     [-2.00000000, -0.70710678,  0.00000000],
     [-1.60000000, -1.41421356,  0.00000000],
     [-0.40000000, -2.12132034,  0.00000000],
     [ 0.40000000, -2.12132034,  0.00000000],
     [ 1.60000000, -1.41421356,  0.00000000],
     [ 2.00000000, -0.70710678,  0.00000000],
 #Cluster  5
     [ 2.40000000,  0.00000000,  0.00000000],
     [ 1.20000000,  2.12132034,  0.00000000],
     [-1.20000000,  2.12132034,  0.00000000],
     [-2.40000000,  0.00000000,  0.00000000],
     [-1.20000000, -2.12132034,  0.00000000],
     [ 1.20000000, -2.12132034,  0.00000000],
 #Cluster  6
     [ 2.40000000,  1.41421356,  0.00000000],
     [ 0.00000000,  2.82842712,  0.00000000],
     [-2.40000000,  1.41421356,  0.00000000],
     [-2.40000000, -1.41421356,  0.00000000],
     [ 0.00000000, -2.82842712,  0.00000000],
     [ 2.40000000, -1.41421356,  0.00000000],
 #Cluster  7
     [ 2.80000000,  0.70710678,  0.00000000],
     [ 2.00000000,  2.12132034,  0.00000000],
     [ 0.80000000,  2.82842712,  0.00000000],
     [-0.80000000,  2.82842712,  0.00000000],
     [-2.00000000,  2.12132034,  0.00000000],
     [-2.80000000,  0.70710678,  0.00000000],
     [-2.80000000, -0.70710678,  0.00000000],
     [-2.00000000, -2.12132034,  0.00000000],
     [-0.80000000, -2.82842712,  0.00000000],
     [ 0.80000000, -2.82842712,  0.00000000],
     [ 2.00000000, -2.12132034,  0.00000000],
     [ 2.80000000, -0.70710678,  0.00000000],
 #Cluster  8
     [ 3.20000000,  0.00000000,  0.00000000],
     [ 1.60000000,  2.82842712,  0.00000000],
     [-1.60000000,  2.82842712,  0.00000000],
     [-3.20000000,  0.00000000,  0.00000000],
     [-1.60000000, -2.82842712,  0.00000000],
     [ 1.60000000, -2.82842712,  0.00000000],
 #Cluster  9
     [ 3.20000000,  1.41421356,  0.00000000],
     [ 2.80000000,  2.12132034,  0.00000000],
     [ 0.40000000,  3.53553391,  0.00000000],
     [-0.40000000,  3.53553391,  0.00000000],
     [-2.80000000,  2.12132034,  0.00000000],
     [-3.20000000,  1.41421356,  0.00000000],
     [-3.20000000, -1.41421356,  0.00000000],
     [-2.80000000, -2.12132034,  0.00000000],
     [-0.40000000, -3.53553391,  0.00000000],
     [ 0.40000000, -3.53553391,  0.00000000],
     [ 2.80000000, -2.12132034,  0.00000000],
     [ 3.20000000, -1.41421356,  0.00000000],
 #Cluster  10
     [ 3.60000000,  0.70710678,  0.00000000],
     [ 2.40000000,  2.82842712,  0.00000000],
     [ 1.20000000,  3.53553391,  0.00000000],
     [-1.20000000,  3.53553391,  0.00000000],
     [-2.40000000,  2.82842712,  0.00000000],
     [-3.60000000,  0.70710678,  0.00000000],
     [-3.60000000, -0.70710678,  0.00000000],
     [-2.40000000, -2.82842712,  0.00000000],
     [-1.20000000, -3.53553391,  0.00000000],
     [ 1.20000000, -3.53553391,  0.00000000],
     [ 2.40000000, -2.82842712,  0.00000000],
     [ 3.60000000, -0.70710678,  0.00000000]]

# posaux    = np.zeros((len(atomlist),len(atompos),11), dtype=np.float32)
max_num_neighb=1000
posaux = np.zeros((len(atomlist),max_num_neighb,11), dtype=np.float32)

for atomi, atomlistitem in enumerate(atomlist):
   print "Atom", atomlistitem
   for k, component  in enumerate(["x","y","z"]):
      # allfilenames=glob.glob('./magnetization_'+component+'/complet/*_'+str(atomlistitem)+'_*/SYSTEM*/Jij.atom*')
      allfilenames=glob.glob('./magnetization_'+component+'/*_'+str(atomlistitem)+'_*/SYSTEM*/Jij.atom*')
      counter = 0
      
      if k==0:
         atomj = []
      
      for filename in enumerate(allfilenames):
         print filename
         file = open(filename[1])
         lines = file.readlines()
         
         # Coordinates of the vectors
         RR = []
         Jij= []
         Rx = []
         Ry = []
         Rz = []
         jj = []
         DD  = []

         # Read data columns into the respective arrays
         for line in lines[0:1000]:
             if not line.startswith("#"):
               # print line.rstrip()
               data_str = line.split()
               RR.append(float(data_str[0]))
               Jij.append(float(data_str[1]))
               DD.append(float(data_str[2]))
               Rx.append(float(data_str[5]))
               Ry.append(float(data_str[6]))
               Rz.append(float(data_str[7]))
               jj.append(float(data_str[8]))
               atj=int(data_str[8])

         positions = np.zeros((len(Rx), 7), dtype=np.float32)
         positions[:, 0] = RR
         positions[:, 1] = Rx
         positions[:, 2] = Ry
         positions[:, 3] = Rz
         positions[:, 4] = DD
         positions[:, 5] = jj
         positions[:, 6] = Jij

         for i, position in enumerate(positions):

            if sort_by_clusters :
               for cluster in range(len(clusterdist)):
                  #Check whether it belongs to the cluster
                  if abs(position[0]-clusterdist[cluster]) < 0.15:
                     if k == 0 :
                        atomj.append(atj)

                     #Sorting
                     for j, atompo in enumerate(atompos):
                         if sum(abs(position[1:4] - atompo)) < 0.1:
                           posaux[atomi,j,0:4] = position[0:4]
                           posaux[atomi,j,k+4] = position[4]
                           posaux[atomi,j,7] = position[5]
                           posaux[atomi,j,k+8] = position[6]
                           counter += 1
            else :
               if k == 0 :
                  atomj.append(atj)
               posaux[atomi,counter,0:4] = position[0:4]
               posaux[atomi,counter,k+4] = position[4]
               posaux[atomi,counter,7] = position[5]
               posaux[atomi,counter,k+8] = position[6]
               counter += 1

      print "Number of neighbour for atom", atomlistitem, "is", counter+1

   # print
   # print
   print "___________________________________________________"
   print "No. links ", 3*counter, " for atom", atomlistitem
   # print posaux[atomi,:,4:8]
   exit()

   counter = 0
   for i, pos in enumerate(posaux[atomi]):
   # for i in range(counter) :
      pos = posaux[atomi,i,:]
      atomj = int(pos[7])
      print
      print "Dij collected", " i", atomlistitem, " j", atomj
      print pos[1:4]
      if atomj in atomlist:
         atomj = atomlist.index(atomj)

         if sort_by_clusters :
            #Sorting
            for j, atompo in enumerate(atompos):
               # print "hexagon site", j, atompo
               if sum(abs(-pos[1:4] - atompo)) < 0.1:
                  # print "i", atomlistitem, " - j", int(pos[7])
                  # print "pos", pos[1:4]
                  # print "atompo", atompo
                  posaux[atomj,j,0]   =  pos[0]
                  posaux[atomj,j,1:7] = -pos[1:7]
                  posaux[atomj,j,7] = atomlistitem
                  posaux[atomj,j,8:11] = pos[8:11]
         else :
               posaux[atomj,counter,0]   =  pos[0]
               posaux[atomj,counter,1:7] = -pos[1:7]
               posaux[atomj,counter,7] = atomlistitem
               posaux[atomj,counter,8:11] = pos[8:11]
               counter += 1


np.set_printoptions(precision=8)
# np.set_printoptions(suppress=True)


for j, atomitem in enumerate(atomlist):
   print "Atom", atomitem, "Rx              Ry              Rz              Dx              Dy              Dz              Jx              Jy              Jz      "
   target.write( "Atom "+ str(atomitem)+ " Rx              Ry              Rz              Dx              Dy              Dz              Jx              Jy              Jz      \n" )
   for i, pos in enumerate(posaux[j]):
      if np.linalg.norm(pos[0:3]) < 0.001:
         continue
      print "%16.8e"*len(pos[1:7]) % tuple(pos[1:7])+"%16.8e"*len(pos[8:11]) % tuple(pos[8:11]) 
      target.write( "%16.8e"*len(pos[1:7]) % tuple(pos[1:7])+"%16.8e"*len(pos[8:11]) % tuple(pos[8:11]) + "\n" )





