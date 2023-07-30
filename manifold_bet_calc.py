import json
jsonstr = '{"id":"48VjzAA3jVFfIb5WLYQS","creatorId":"tX8upfYRryXATWlLNrSi0wpbtrW2","creatorUsername":"DavidLawrence","creatorName":"David Lawrence","createdTime":1674776230937,"creatorAvatarUrl":"https://lh3.googleusercontent.com/a/AEdFTp66p9lmGBdH2GpLQP6A6Ta2pkYWD7eBXIe0xaWT=s96-c","closeTime":1735689540000,"question":"Will TikTok be banned in the United States for the majority of the population by the end of 2024?","url":"https://manifold.markets/DavidLawrence/will-tiktok-be-banned-in-the-united","pool":{"NO":1679.1949360854742,"YES":1874.901940996789},"probability":0.26999999999999996,"p":0.29227081568264524,"totalLiquidity":1770,"outcomeType":"BINARY","mechanism":"cpmm-1","volume":15205.153940999196,"volume24Hours":0,"isResolved":false,"lastUpdatedTime":1688655951288,"description":{"type":"doc","content":[{"type":"paragraph","content":[{"text":"This question is about the legislation impacting consumers before the end of 2024 (for the majority of Americans). ","type":"text"}]},{"type":"bulletList","content":[{"type":"listItem","content":[{"type":"paragraph","content":[{"text":"If TikTok is banned for the majority of Americans before the end of 2024 and some people were still accessing TikTok illegally in the US after the ban came into place then the market would resolve YES","type":"text"}]}]},{"type":"listItem","content":[{"type":"paragraph","content":[{"text":"If a bill is signed into law but is not yet impacting consumers (i.e. because it is held up in court) that would ","type":"text"},{"text":"not ","type":"text","marks":[{"type":"bold"}]},{"text":"count towards a YES because the ban would not yet be impacting consumers","type":"text"}]}]},{"type":"listItem","content":[{"type":"paragraph","content":[{"text":"If TikTok is banned in a way that impacted the majority of Americans before the end of 2024, then the market would resolve as a YES (even if TikTok was later re-instated)","type":"text"}]}]}]}]},"textDescription":"This question is about the legislation impacting consumers before the end of 2024 (for the majority of Americans). \n\nIf TikTok is banned for the majority of Americans before the end of 2024 and some people were still accessing TikTok illegally in the US after the ban came into place then the market would resolve YES\n\nIf a bill is signed into law but is not yet impacting consumers (i.e. because it is held up in court) that would not count towards a YES because the ban would not yet be impacting consumers\n\nIf TikTok is banned in a way that impacted the majority of Americans before the end of 2024, then the market would resolve as a YES (even if TikTok was later re-instated)"}'

slug_json = json.loads(jsonstr, strict = False)
pool = slug_json['pool']
p = slug_json['p']

def getCpmmProbability(pool, p):
  YES = pool['YES']
  NO = pool['NO']
  return (p * NO) / (((1 - p) * YES) + (p * NO))

def addCpmmLiquidity(pool, p):
    prob = getCpmmProbability(pool, p)
    y = pool['YES']
    n = pool['NO']
    numerator = y * prob
    denominator = (y * prob) - (n * (prob - 1))
    post_bet_p = numerator / denominator
    return post_bet_p

def calculateCpmmPurchase(pool, p, bet):
    bet_amount = bet['amount']
    bet_outcome = bet['outcome']
    bet_shares = calculateCpmmShares(pool, p, bet_outcome, bet_amount)
    bet['shares'] = bet_shares

    y = pool['YES']
    n = pool['NO']
    if bet_outcome == 'YES':
        newY = y - bet_shares + bet_amount
        newN = n + bet_amount
    else:
        newY = y + bet_amount
        newN = n - bet_shares + bet_amount
    post_bet_pool = {}
    post_bet_pool['YES'] = newY
    post_bet_pool['NO'] = newN
    post_bet_p = addCpmmLiquidity(post_bet_pool, p)
    return bet, post_bet_pool, post_bet_p

# before liquidity fee
def calculateCpmmShares(pool, p, bet_outcome, bet_amount):
    y = pool['YES']
    n = pool['NO']
    k = (y ** p) * (n ** (1 - p))
    if bet_outcome == 'YES':
        shares = y + bet_amount - (k * ((bet_amount + n) ** (p - 1))) ** (1 / p)
    else:
        shares = n + bet_amount - (k * ((bet_amount + y) ** -p)) ** (1 / (1 - p))
    return shares

def getProbability(pool, p):
    return (p * pool['NO']) / (((1 - p) * pool['YES']) + (p * pool['NO']));

def calculateFixedMktPayout(p, bet):
    bet_outcome = bet['outcome']
    shares = bet['shares']
    if bet_outcome == 'YES':
        betP = p
    else:
        betP = 1 - p
    return betP * shares

bet = {}
bet['outcome'] = 'YES'

bet['amount'] = 200
[bet, post_bet_pool, post_bet_p] = calculateCpmmPurchase(pool, p, bet)
calculateFixedMktPayout(post_bet_p, bet)
prob = getCpmmProbability(post_bet_pool, post_bet_p)
print(f"Original pool: {pool}")
print(f"Original p: {p}")
print(f"Post bet pool: {post_bet_pool}")
print(f"Post bet p: {post_bet_p}")
print(f"Post bet probability: {prob}")
print(f"Bet: {bet}")
