export interface User_Create_Response_POST
{
    id: number,
    username: string,
    level: number,
    cosmetics: Cosmetic[],
    tasks: Task[]
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

export interface User_GetShop_Response_GET
{
    cosmetics: Cosmetic[];
}

export interface User_BuyCosmetic_Response_PATCH
{
    inventory: Cosmetic[];
}
export interface Cosmetic{
    name: string,
    price: number,
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