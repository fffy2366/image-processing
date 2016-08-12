%===============================================================================
%函数名称：face_segment
%输入参数：mImageSrc，待分割的人脸图像，可能是灰度图像，也可能是彩色图像
%输出参数：mFaceResult，分割后的人脸结果，应为灰度图像
%主要步骤：1）进行人脸检测，得到脸部区域的框框
%         2）得到脸部图像框的中心点
%         3）根据中心点，对图像进行等比例外扩，得到合适大小的人脸图像
%注意事项：1)首先需要判断该图像是否为灰度图，若为灰度图，需要先将其转换为三通道彩色图
%===============================================================================
function mFaceResult = face_segment(mImageSrc)
%%%%%%%%%%%%%%%%%%%%将灰度图变为三通道图%%%%%%%%%%%%%%%%%%%%
if(size(mImageSrc,3) == 1)
    mImage2detect(:,:,1) = mImageSrc;
    mImage2detect(:,:,2) = mImageSrc;
    mImage2detect(:,:,3) = mImageSrc;
else
    mImage2detect = mImageSrc;
end

%%%%%%%%%%%%%%%%%%%%对图像进行人脸检测%%%%%%%%%%%%%%%%%%%%
FaceDetector               = buildDetector();
[bbox,bbimg,faces,bbfaces] = detectFaceParts(FaceDetector,mImage2detect,2);

%%%%%%%%%%%%%%%%%%%%输入图像灰度化%%%%%%%%%%%%%%%%%%%%
if 1 ~= size(mImageSrc,3)
    mImageSrc = rgb2gray(mImageSrc);
    mImageSrc = double(mImageSrc);
elseif 1     == size(mImageSrc,3)
    mImageSrc = double(mImageSrc);
end

%%%%%%%%%%%%%%%%%%%%得到人脸区域框的中心点%%%%%%%%%%%%%%%%%%%%
recFace.x          = bbox(1,1);
recFace.y          = bbox(1,2);
recFace.width      = bbox(1,3);
recFace.height     = bbox(1,4);

ptFaceCenter.x     = recFace.x + recFace.width / 2;
ptFaceCenter.y     = recFace.y + recFace.height / 2;

%%%%%%%%%%%%%%%%%%%%以中心点为基准进行外扩（即对人脸选框进行调整）%%%%%%%%%%%%%%%%%%%%
recFace.x         = ptFaceCenter.x - recFace.width * 0.4;
recFace.y         = ptFaceCenter.y - recFace.height * 0.35;
recFace.width     = recFace.width * 0.8 ;
recFace.height    = recFace.height * 0.8 ;

mFaceResult       = uint8(imcrop(mImageSrc,[recFace.x,recFace.y,recFace.width,recFace.height]));
end