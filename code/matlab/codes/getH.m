function H = getH(G)
	% get dimensions
	[k, n] = size(G);
	
	% extract parity matrix
	P = G(:, k + 1:n);

	% calculate check matrix and return
	H = [P', eye(n - k)];
end
