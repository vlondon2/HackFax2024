import { Routes } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { SignInComponent } from './components/sign-in/sign-in.component';

export const routes: Routes = [
    {path: '', component: SignInComponent},
    {path: 'home', component: HomeComponent}
];
