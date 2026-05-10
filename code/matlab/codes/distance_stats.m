function [min, max] = distance_stats(G)
	% get dimensions
	[k, n] = size(G);

	% get alphabet
	alph = get_alphabet(G);
	c_words = alph(:, k + 1:n + k);

	% get min and max weight
	min = max = weight(c_words(2, :));
	for i = 3:size(c_words, 1)
		w = weight(c_words(i, :));
		if w < min
			min = w;
		end
		if w > max
			max = w;
		end
	end
end
