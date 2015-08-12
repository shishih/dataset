% read the useful frames and cut video

record=load('790.txt');

videoname='790.mp4';
% record is the matrix of frames without face
[row,col]=size(record);
readobj=VideoReader(videoname);
% vidFrames=read(readobj);

numFrames=get(readobj,'NumberOfFrames');
frameRate=get(readobj,'FrameRate');
record(row+1,1)=numFrames;

begin=1;
for i =2:row+1
    if record(i)-record(i-1)<50
        continue;
    else
        [temp,len]=size(videoname);
        name=[videoname(1:len-4),'_',mat2str(begin),'_',mat2str(record(i))];
        outObj=VideoWriter(name,'MPEG-4');
        outObj.FrameRate=frameRate;
        open(outObj);
        writeVideo(outObj,read(readobj,[begin record(i)]));
        begin=record(i)+1;
        close(outObj);
    end        
end
  

