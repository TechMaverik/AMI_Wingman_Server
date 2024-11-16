#! /bin/bash
echo '*** A.M.I DRONE SIMULATOR ***'
echo 'FC: CubeOrange'
sim_vehicle.py --console  --out=udp:127.0.0.1:1992 -v ArduCopter
