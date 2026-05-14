function x = ml_decode(G, y)
	% get dimensions
	[k, n] = size(G);

	% get alphabet
	alph = get_alphabet(G);
	c_words = alph(:, k + 1:n + k);

	% get min distance 
	min = distance(c_words(1, :), y);
	idx = 1;
	for i = 2:size(c_words, 1)
		w = distance(c_words(i, :), y);
		if w < min
			min = w;
			idx = i;
		end
	end

	x = c_words(idx, :);
end
