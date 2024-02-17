import { Routes } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { SignInComponent } from './components/sign-in/sign-in.component';
import { TaskBoardComponent } from './components/task-board/task-board.component';

export const routes: Routes = [
    {path: '', component: SignInComponent},
    {path: 'home', component: HomeComponent},
    {path: 'tasks', component: TaskBoardComponent}
];
