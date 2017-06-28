function [ res ] = pseudoInv( A )
%pseudoInv: calculate the pseudo-inverse matrix
    tran = A';
    res = inv(tran*A)*tran;

end
