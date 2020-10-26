%MATLAB:KNN algorithum
%2020.10.26--18:35:18

% KNN（K-Nearest Neighbor）算法即K最邻近算法，是实现分类器中比较简单易懂的一种分类算法。K临近之所以简单是因为它比较符合人们直观感受，即人们在观察事物，对事物进行分类的时候，人们最容易想到的就是谁离那一类最近谁就属于哪一类，即俗话常说的“近朱者赤，近墨者黑”，人们自然而然地把这种观察方式延伸到数据分类处理领域。K-NN算法就是基于欧几里得距离推断事物类别的一种实现方法。
% 
% 描述如下：
% 
% 1、初始化训练集和类别；
% 
% 2、计算测试集样本与训练集样本的欧氏距离；
% 
% 3、根据欧氏距离大小对训练集样本进行升序排序；
% 
% 4、选取欧式距离最小的前K个训练样本，统计其在各类别中的频率；
% 
% 5、返回频率最大的类别，即测试集样本属于该类别。
% 
% 但是，当样本不平衡时，可能导致大多数邻居偏向不正确的结果。
% 为避免这种情形，我们采用加权方式改进



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


% 算法改进：压缩邻居算法
% 产生新的样本集，使得计算数减少，但保留分类器能力。
% 基本思路：定义两个存储器，一个用以存放生成的样本集output，另一个为original。
% 
% 1、初始化：output为空，原始集存入original，再从original中任选其一移动至output；
% 2、original中选择第i个样本，使用output中的样本进行KNN分类。若分类错误，移动至output。
% 3、重复第二步至original遍历完成，output为压缩集。
