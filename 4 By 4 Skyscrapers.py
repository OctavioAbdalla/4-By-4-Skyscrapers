def solve_puzzle(clues):

    mold = [
        [0, clues[0], clues[1], clues[2], clues[3], 0], 
        [clues[15], 0, 0, 0, 0, clues[4]],
        [clues[14], 0, 0, 0, 0, clues[5]],
        [clues[13], 0, 0, 0, 0, clues[6]],
        [clues[12], 0, 0, 0, 0, clues[7]],
        [0, clues[11], clues[10], clues[9], clues[8], 0]
    ]

    possib_ans = [
        (1, 4, 1, 2, 3, 2),
        (1, 4, 2, 1, 3, 2),
        (1, 4, 2, 3, 1, 3),
        (1, 4, 1, 3, 2, 3),
        (1, 4, 3, 1, 2, 3),
        (1, 4, 3, 2, 1, 4),
        (2, 3, 2, 1, 4, 1),
        (2, 3, 1, 2, 4, 1),
        (2, 3, 2, 4, 1, 2),
        (2, 3, 1, 4, 2, 2),
        (2, 1, 4, 2, 3, 2),
        (2, 3, 4, 1, 2, 2),
        (2, 2, 1, 4, 3, 2),
        (2, 2, 4, 1, 3, 2),
        (2, 2, 4, 3, 1, 3),
        (2, 1, 4, 3, 2, 3),
        (2, 3, 4, 2, 1, 3),
        (3, 2, 3, 4, 1, 2),
        (3, 1, 3, 2, 4, 1),
        (3, 1, 2, 4, 3, 2),
        (3, 1, 3, 4, 2, 2),
        (3, 2, 3, 1, 4, 1),
        (3, 2, 1, 3, 4, 1),
        (4, 1, 2, 3, 4, 1),
    ]
    
    
    game_complete = False 
    
    while game_complete == False:       
        
        game_complete = True
        
        def matching_results(result_to_match):
            matching_results = []
            
            for result in possib_ans:
                match = True
                for i in range(len(result)):
                    if isinstance(result_to_match[i], list):
                        if result[i] not in result_to_match[i]:
                            match = False
                            break    
                    elif result_to_match[i] != 0 and result[i] != result_to_match[i]:
                        match = False
                        break
                if match:
                    matching_results.append(result)

            new_tuple = []

            for i in range(len(matching_results[0])):
                elementos = tuple(t[i] for t in matching_results)
                if all(x == elementos[0] for x in elementos):
                    new_tuple.append(elementos[0])
                else:
                    new_tuple.append(list(set(elementos)))
            return tuple(new_tuple)

        for col in range(1,5): 
            column = [row[col] for row in mold]
            column = matching_results(column)  
            for i in range(0,6):
                mold[i][col] = column[i]
                  
        for row in range(1,5):
            new_row = matching_results(mold[row])
            mold[row] = list(new_row)
    
        for rows in mold:
            for columns in rows:
                if not isinstance(columns, int):
                    game_complete = False
                    break
        
        result = []        
        if game_complete == True:
            for row in range(1,5):
                result.append(tuple(mold[row][1:5]))
            result = tuple(result)
    
    return result


solve_puzzle(
( 0, 0, 1, 2,   
  0, 2, 0, 0,   
  0, 3, 0, 0, 
  0, 1, 0, 0 )
    )

