for i in *	
do
	tail -n +3 $i | sponge $i   
done
