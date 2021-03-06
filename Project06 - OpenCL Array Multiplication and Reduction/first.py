#Philip Chang - #6 - first python script
import os

NMB_ARRAY = [1, 10, 50, 100, 200, 500, 700, 1000, 2000, 3000, 4000, 5000, 6000, 8000]
LOCAL_ARRAY = [8, 32, 64, 128, 256, 512]

for nmb in NMB_ARRAY:
    for local in LOCAL_ARRAY:
        cmd = "g++ -DNMB=%d -DLOCAL_SIZE=%d -o first first.cpp /scratch/cuda-7.0/lib64/libOpenCL.so -lm -fopenmp" % (nmb, local)
        os.system(cmd)
        cmd = "./first"
        os.system(cmd)
