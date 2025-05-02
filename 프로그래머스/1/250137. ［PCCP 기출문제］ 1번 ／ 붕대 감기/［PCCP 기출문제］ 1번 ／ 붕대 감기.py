def solution(bandage, health, attacks):
    def calc_heal(time):
        return time * bandage[1] + (time // bandage[0]) * bandage[2]
        
    h = health
    t = 0
    for attack_t, attack_h in attacks:
        skill_t = attack_t - t - 1
        h = min(health, h + calc_heal(skill_t)) - attack_h
        
        if h <= 0: break
        t = attack_t
    
    return h if h > 0 else -1