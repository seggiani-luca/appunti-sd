function w = distance(a)
	% get size
	[~, n] = size(a);

	% create zero vector
	z = zeros(1, n);

	% get distance
	w = distance(a, z);
end
