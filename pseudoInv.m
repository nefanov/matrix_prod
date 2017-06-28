function [ res ] = pseudoInv( A )
%pseudoInv: calculate the pseudo-inverse matrix
    tran = A';
    res = INV(tran*A)*tran;

end

