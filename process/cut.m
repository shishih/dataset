% read the useful frames and cut video

videoname='9.mp4';
% record is the matrix of frames without face
[row,col]=size(record);
readobj=VideoReader(videoname);
% vidFrames=read(readobj);

numFrames=get(readobj,'NumberOfFrames');
frameRate=get(readobj,'FrameRate');

for i =2:row
    if record(i)-record(i-1)<300
        continue;
    else
        [temp,len]=size(videoname);
        name=[videoname(1:len-4),'_',mat2str(record(i-1))];
        outObj=VideoWriter(name,'MPEG-4');
        outObj.FrameRate=frameRate;
        open(outObj);
        writeVideo(outObj,read(readobj,[record(i-1) record(i)]));
        close(outObj);
    end
end
  

