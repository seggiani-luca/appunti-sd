function G = getG(H)
	% get dimensions
	[n_k, n] = size(H);
	k = n - n_k;

	% extract pariy matrix
	P_T = H(:, 1:k);

	% calculate generator matrix and return
	G = [eye(k), P_T'];
end
