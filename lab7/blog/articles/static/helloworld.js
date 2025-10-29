let groupmates = [
        {
            "name": "Анастасия",
            "surname": "Пахомова",
            "exams": ["АиГ", "МИСПиСИТ", "АИС"],
            "group": "БСТ2203",
            "marks": [5, 5, 3]
        },
        {
            "name": "Никита",
            "surname": "Парфенов",
            "exams": ["АиГ", "МИСПиСИТ", "АИС"],
            "group": "БВТ2203",
            "marks": [5, 5, 5]
        },
        {
            "name": "Филипп",
            "surname": "Гилёв",
            "exams": ["АиГ", "МИСПиСИТ", "АИС"],
            "group": "БВТ2203",
            "marks": [5, 5, 5]
        },
        {
            "name": "Светлана",
            "surname": "Озюменко",
            "exams": ["АиГ", "МИСПиСИТ", "АИС"],
            "group": "БСТ2203",
            "marks": [5, 5, 4]
        }
]

let rpad = function(str, length) {
    str = String(str);
    while (str.length < length)
        str += ' ';
    return str;
}

let printGroupmates = function(groupmates) {
    console.log(
        rpad("name", 15),
        rpad("surname", 15),
        rpad("exams", 15),
        rpad("group", 8),
        rpad("marks", 20)
    );

    for (let i = 0; i <= groupmates.length-1; i++) {
        console.log(
            rpad(groupmates[i]['name'], 15),
            rpad(groupmates[i]['surname'], 15),
            rpad(groupmates[i]['exams'], 15),
            rpad(groupmates[i]['group'], 8),
            rpad(groupmates[i]['marks'], 20),
        );
    }
    console.log('\n')
}

printGroupmatesFilteredByGroup = function(groupmates, targetGroup) {
        console.log(
        rpad("name", 15),
        rpad("surname", 15),
        rpad("exams", 15),
        rpad("group", 8),
        rpad("marks", 20)
    );

    for (let i = 0; i <= groupmates.length-1; i++) {
        if (groupmates[i]['group'] == targetGroup)
            console.log(
                rpad(groupmates[i]['name'], 15),
                rpad(groupmates[i]['surname'], 15),
                rpad(groupmates[i]['exams'], 15),
                rpad(groupmates[i]['group'], 8),
                rpad(groupmates[i]['marks'], 20),
            );
    }
    console.log('\n')
}

// printGroupmatesFilteredByAverageMark = function(groupmates, targetGroup) {
//         console.log(
//         rpad("name", 15),
//         rpad("surname", 15),
//         rpad("exams", 15),
//         rpad("group", 8),
//         rpad("marks", 20)
//     );

//     for (let i = 0; i <= groupmates.length-1; i++) {
//         if (groupmates[i]['group'] == targetGroup)
//             console.log(
//                 rpad(groupmates[i]['name'], 15),
//                 rpad(groupmates[i]['surname'], 15),
//                 rpad(groupmates[i]['exams'], 15),
//                 rpad(groupmates[i]['group'], 8),
//                 rpad(groupmates[i]['marks'], 20),
//             );
//     }
//     console.log('\n')
// }

printGroupmates(groupmates)
printGroupmatesFilteredByGroup(groupmates, "БСТ2203")