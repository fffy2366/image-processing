function showboxes(im, boxes, posemap)

% function showboxes(im, boxes,posemap)
% 
% % showboxes(im, boxes)
% % Draw boxes on top of image.
% 
% clf;
% image(im);
% axis equal;
% axis off;
% grid off;
% c(1)    = {'r'};
% c(2:100) = {'b'};
% xgroup = zeros(1,100);
% ygroup = zeros(1,100);
% 
% for b = boxes,
%     for i = size(b.xy,1):-1:1;
%         
%         x1 = b.xy(i,1);
%         y1 = b.xy(i,2);
%         x2 = b.xy(i,3);
%         y2 = b.xy(i,4);
%         line([x1 x1 x2 x2 x1]', [y1 y2 y2 y1 y1]', 'color', c{i}, 'linewidth', 2);
%         plot((x1+x2)/2,(y1+y2)/2,'r.','markersize',15);
%       xgroup(x1,i) = x1;  
%         
%         
%     end
%     
% end
% %       x1min = min(xgroup);
% %       x1max = max(xgroup);
% %       y1min = min(ygroup);
% %       y1max = max(ygroup);  
% %       line([x1min x1min x1max x1max x1min]', [y1min y1max y1max y1min ymin]', 'color', 'r', 'linewidth', 2);
%       
% drawnow;


% showboxes(im, boxes)
% Draw boxes on top of image.

imagesc(im);

hold on;
axis image;
axis off;

for b = boxes,
    partsize = b.xy(1,3)-b.xy(1,1)+1;

    tx = (min(b.xy(:,1)) + max(b.xy(:,3)))/2;
    ty = min(b.xy(:,2)) - partsize/2;
    text(tx,ty, num2str(posemap(b.c)),'fontsize',18,'color','c');
   
%     for i = size(b.xy,1):-1:1;
% 
%         x1 = b.xy(i,1);
%         y1 = b.xy(i,2);
%         x2 = b.xy(i,3);
%         y2 = b.xy(i,4);
    for i = size(b.xy,1):-1:1;

        x1 = b.xy(i,1);
        y1 = b.xy(i,2);
        x2 = b.xy(i,3);
        y2 = b.xy(i,4);


        line([x1 x1 x2 x2 x1]', [y1 y2 y2 y1 y1]', 'color', 'b', 'linewidth', 1);
        
        plot((x1+x2)/2,(y1+y2)/2,'r.','markersize',15);
        
        
        
        
    end
   xx1 =min(b.xy(:,1))+20;
   xx2 =max(b.xy(:,3))-20;
   yy1 =min(b.xy(:,2))+20;
   yy2 =max(b.xy(:,4))-20;
   line([xx1 xx1 xx2 xx2 xx1]', [yy1 yy2 yy2 yy1 yy1]', 'color', 'g', 'linewidth', 2);
   
   imwrite(imcrop(im,[xx1 yy1 xx2-xx1 yy2-yy1]),'d:\pic001.jpg');
   
end
   
   
%     line([x11 x11 x21 x21 x11]', [y11 y21 y21 y11 y11]', 'color', 'r', 'linewidth', 2);

drawnow;
