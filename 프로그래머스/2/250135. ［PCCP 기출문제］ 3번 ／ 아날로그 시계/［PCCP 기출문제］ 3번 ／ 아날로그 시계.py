def calc_deg(h, m, s):
        h_deg = (h % 12) * 30 + m * (1/2) + s * (1/120)
        m_deg = m * 6 + s * (1/10)
        s_deg = s * 6
        
        return h_deg, m_deg, s_deg

def solution(h1, m1, s1, h2, m2, s2):
    ans = 0
    
    h_deg, m_deg, s_deg = calc_deg(h1, m1, s1)
    
    start = h1 * 3600 + m1 * 60 + s1 + 1
    end = h2 * 3600 + m2 * 60 + s2
    for t in range(start, end + 1):
        nh = t // 3600
        nm = (t % 3600) // 60
        ns = t % 60
        
        nh_deg, nm_deg, ns_deg = calc_deg(nh, nm, ns)
        if h_deg > nh_deg: nh_deg += 360
        if m_deg > nm_deg: nm_deg += 360
        if s_deg > ns_deg: ns_deg += 360
        
        cnt = 0
        if s_deg <= m_deg and ns_deg > nm_deg: cnt += 1
        if s_deg <= h_deg and ns_deg > nh_deg: cnt += 1
        if cnt == 2 and m_deg <= h_deg and nm_deg > nh_deg: cnt -= 1
        ans += cnt
        
        h_deg = nh_deg % 360
        m_deg = nm_deg % 360
        s_deg = ns_deg % 360
        
    cnt = 0
    if s_deg == m_deg: cnt += 1
    if s_deg == h_deg: cnt += 1
    if cnt == 2 and m_deg == h_deg: cnt -= 1
    ans += cnt
        
    return ans