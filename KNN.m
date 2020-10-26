%MATLAB:KNN algorithum
%2020.10.26--18:35:18

% KNN��K-Nearest Neighbor���㷨��K���ڽ��㷨����ʵ�ַ������бȽϼ��׶���һ�ַ����㷨��K�ٽ�֮���Լ�����Ϊ���ȽϷ�������ֱ�۸��ܣ��������ڹ۲������������з����ʱ�������������뵽�ľ���˭����һ�����˭��������һ�࣬���׻���˵�ġ������߳࣬��ī�ߺڡ���������Ȼ��Ȼ�ذ����ֹ۲췽ʽ���쵽���ݷ��ദ������K-NN�㷨���ǻ���ŷ����þ����ƶ���������һ��ʵ�ַ�����
% 
% �������£�
% 
% 1����ʼ��ѵ���������
% 
% 2��������Լ�������ѵ����������ŷ�Ͼ��룻
% 
% 3������ŷ�Ͼ����С��ѵ��������������������
% 
% 4��ѡȡŷʽ������С��ǰK��ѵ��������ͳ�����ڸ�����е�Ƶ�ʣ�
% 
% 5������Ƶ��������𣬼����Լ��������ڸ����
% 
% ���ǣ���������ƽ��ʱ�����ܵ��´�����ھ�ƫ����ȷ�Ľ����
% Ϊ�����������Σ����ǲ��ü�Ȩ��ʽ�Ľ�



    %First solution:KNN with weight

set1=rand(3,50);
set2=rand(3,50)+0.7;
set3=rand(3,50)+1.5;
dataset=[set1 set2 set3];
label=[ones(1,50) 2*ones(1,50) 3*ones(1,50)];
t=rand(3,8)*2.5;

[fea,num]=size(dataset);
dist=[];
    %caculate the Euclidean distance
for i=1:num
    sum=0;
    for j=1:fea
        sum=sum+(t(j)-dataset(j,i))^2;
    end
    dist(i)=sqrt(sum);
end

K=3;    %order the const K
sorteddist=sort(dist);
ct1=0;ct2=0;ct3=0;

for i=1:K
    tarind=find(sorteddist(i)==dist);
    if label(tarind)==1
        ct1=ct1+1/sorteddist(i);
    else if label(tarind)==2
            ct2=ct2+1/sorteddist(i);
         else ct3=ct3+1/sorteddist(i);
        end
    end
end

maxc=max([ct1,ct2,ct3]);
tarind=find(maxc==[ct1 ct2 ct3])

figure;     %create a figure window
hold on
plot(dataset(1,1:50),dataset(2,1:50),'r.','Markersize',12)
plot(dataset(1,51:100),dataset(2,51:100),'g.','Markersize',12)
plot(dataset(1,101:150),dataset(2,101:150),'.','Markersize',12)
plot(t(1),t(2),'*','Markersize',12)


% �㷨�Ľ���ѹ���ھ��㷨
% �����µ���������ʹ�ü��������٣�������������������
% ����˼·�����������洢����һ�����Դ�����ɵ�������output����һ��Ϊoriginal��
% 
% 1����ʼ����outputΪ�գ�ԭʼ������original���ٴ�original����ѡ��һ�ƶ���output��
% 2��original��ѡ���i��������ʹ��output�е���������KNN���ࡣ����������ƶ���output��
% 3���ظ��ڶ�����original������ɣ�outputΪѹ������
