function alphabet = get_alphabet(G)
	function b = count(b)
		for i_k = 0:k - 1
			% sum
			b(1, k - i_k) = b(1, k - i_k) + 1;

			% carry
			if b(1, k - i_k) == 2
				b(1, k - i_k) = 0;
			else 
				return
			end
		end
	end

	function a = gf(a)
		a = mod(a, 2);
	end

	% get dimensions
	[k, n] = size(G);
	num = 2.^k;

	% fill a matrix
	alphabet = zeros(num, k + n);

	% count words
	b = zeros(1, k);
	for i = 1:num
		% get code
		c = gf(b * G);

		% append
		alphabet(i, :) = [b, c];

		% count
		b = count(b);
	end
end
