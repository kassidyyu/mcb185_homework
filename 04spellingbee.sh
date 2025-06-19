gunzip -c ../MCB185/data/dictionary.gz | grep -v "[^rzoniac]" | grep -E "r" | grep -E ".{4,}"
