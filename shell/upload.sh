#push git
git add /Users/apple/Desktop/Workspace/Python/demos/gitPython/
git commit -m "自动上传+"+$@
git push origin master

#server pull
curl 120.27.51.48:8888

#print result
echo "upload success\n"
