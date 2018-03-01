#!/bin/bash
basepath=`pwd` #获取当前执行脚本的文件路径
if [ $# -ne 2 ] 
then
	echo "param error!"
	exit
fi
echo "use pattern $1 to filter files"
for file in `ls ${basepath}|egrep $1`
do
		echo "copy ${file} to $2"
		scp "${basepath}/${file}" "$2"   
done
