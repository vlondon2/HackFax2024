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

export interface User_CompleteTask_Response_PATCH
{
    removed: Task,
    tasks: Task[],
    xp: number,
    level: number,
    lvlxp: number,
    gold: number
}

export interface User_GetShop_Response_PATCH
{
    availableCosmetics: Cosmetic[];
}

export interface Cosmetic{
    name: string,
    price: 10,
    path: string,
    requiredlvl: number
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