function solution(participant, completion) {
    participant = participant.sort();
    completion = completion.sort();
    
    const LENGTH = completion.length;
    let i = 0;
    for (i = 0; i < LENGTH; i++) {
        if (participant[i] !== completion[i]) break;
    }
    
    return participant[i];
}