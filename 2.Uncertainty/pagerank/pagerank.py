import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    result = dict.fromkeys(list(corpus.keys()), 0)
    linked = len(corpus[page])

    for i in corpus[page]:
        result[i] = damping_factor / linked

    total = len(corpus)
    for k in corpus.keys():
        result[k] += (1 - damping_factor) / total

    return result
    # raise NotImplementedError


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    rank = dict.fromkeys(list(corpus.keys()), 0)
    page = random.choice(list(corpus.keys()))
    rank[page] += 1

    # page = '1.html'
    # corpus = {"1.html": {"2.html", "3.html"},
    #           "2.html": {"3.html"}, "3.html": {"2.html"}}
    # transition_model(corpus, page, damping_factor)

    for i in range(1, n):
        model = transition_model(corpus, page, damping_factor)

        page = random.choices(
            list(corpus.keys()), weights=list(model.values()))[0]

        rank[page] += 1

        # for k, v in transition_model(corpus, s, damping_factor).items():
        #     model[k] += v

    for k in rank.keys():
        rank[k] /= n

    return rank
    # raise NotImplementedError


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """

    convergence = 0.001
    N = len(corpus)
    rank = dict.fromkeys(list(corpus.keys()), 1 / N)

    while True:
        size = 0
        for key in corpus:
            condition1 = (1 - damping_factor) / N
            condition2 = 0

            for i in corpus:
                if key in corpus[i]:
                    numLinks = len(corpus[i])
                    condition2 += (rank[i] / numLinks)

            curr = condition1 + damping_factor * condition2

            if abs(rank[key] - curr) < convergence:
                size += 1

            rank[key] = curr

        if size == N:
            break

    return rank

    # raise NotImplementedError


if __name__ == "__main__":
    main()
