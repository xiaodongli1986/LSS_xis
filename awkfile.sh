
for zstr in 0 0.5 1 1.5 2
do
nowfile=J08.dat.z_$zstr.mge3.000e11.slice1.1
awk < $nowfile '{if($1<800 && $2 < 800) print $1,$2}' >> $nowfile.part
done

