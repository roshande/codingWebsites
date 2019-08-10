struct trie{
    int words;
    int prefixes;
    struct trie edges[26];
} trie;

void initialize(trie vertex)
{
    vertex.words = 0;
    vertex.prefixes = 0;
    for(int i = 0; i< 26; ++i)
    {
        vertex.edges[i] = NULL;
    }
}

void addWord(trie vertex, char[] word)
{
    if(isEmpty(word))
        vertex.words = vertex.words + 1;
    else
    {
        vertex.prefixes = vertex.prefixes + 1;
        k = fir
    }
            
}
