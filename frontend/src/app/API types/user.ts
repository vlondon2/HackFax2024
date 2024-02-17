export interface User_Create_Response_POST
{
    id: number,
    username: string,
    level: number,
    cosmetics: string[],
    tasks: string[]
}

export interface User_Get_Response_GET
{
    id: number,
    username: string,
    level: number,
    cosmetics: Cosmetic[]
    xp: number,
    lvlxp: number,
    tasks: Task[],
    gold: number
}

export interface Cosmetic{
    name: string,
    price: 10,
    path: string
}

export interface Task{
    name: string,
    description: string,
    xp: number
}

export interface User
{
    id: number,
    username: string,
    level: number,
    cosmetics: Cosmetic[]
    xp: number,
    lvlxp: number,
    tasks: Task[],
    gold: number
}