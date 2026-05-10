function d = distance(a, b)
	% get size
	[~, n1] = size(a);
	[~, n2] = size(b);

	if n1 != n2
		return;
	end

	n = n1;

	% calculate distance
	d = 0;

	for i = 1:n
		if a(1, i) != b(1, i)
			d = d + 1;
		end
	end
end
