load('temp.mat');
motif_num=2;
W=spones(W);
B=W.*W';
U=W-B;
switch(motif_num)
    case 1
        C=U*U.*U';
        C=C+C';
    case 2
        C=(B*U).*U'+(U*B).*U'+(U*U).*B;
        C=C+C';
    case 3
        C=(B*B).*U+(B*U).*B+(U*B).*B;
        C=C+C';
    case 4
        C=(B*B).*B;
    case 5
        C=(U*U).*U+(U*U').*U+(U'*U).*U;
        C=C+C';
    case 6
        C=(U*B).*U+(B*U').*U'+(U'*U).*B;
    case 7
        C=(U'*B).*U'+(B*U).*U+(U*U').*B;
end
W_M=spfun(@(x) 1./(x+1),C).*W;
save('W_M.mat','W_M');
   
        
        