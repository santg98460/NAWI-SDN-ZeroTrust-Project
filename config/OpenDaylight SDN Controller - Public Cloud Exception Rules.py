# OpenDaylight SDN Controller - Public Cloud Exception Rules

# RULE 1: Block cross-border PRIVATE CLOUD access (ALWAYS)
Rule 1 (Priority 1000):
    match: src_region=CANADA, dst=PRIVATE_CLOUD_USA
    action: DROP
    log: TRUE

Rule 2 (Priority 1000):
    match: src_region=USA, dst=PRIVATE_CLOUD_CANADA
    action: DROP
    log: TRUE

# RULE 2: ALLOW cross-border PUBLIC CLOUD access (PUBLIC data only)
Rule 3 (Priority 900):
    match: dst=PUBLIC_CLOUD, data_classification=PUBLIC
    action: ALLOW
    log: TRUE (for audit)

# RULE 3: Block any attempt to access sensitive data from wrong region
Rule 4 (Priority 950):
    match: dst=PUBLIC_CLOUD, data_classification=RESTRICTED
    action: DROP
    log: TRUE (security alert)

# RULE 4: Rate limit public cloud access to prevent abuse
Rule 5 (Priority 800):
    match: dst=PUBLIC_CLOUD, src_region=CANADA
    action: ALLOW (rate-limit: 100 Mbps per user)