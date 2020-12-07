import React from 'react';
import { Link } from 'react-router-dom';

function Login(props) {
    return (
            <div>
               <LoginPanel />
            </div>
    )
}

function LoginPanel(props) {
    return (
        <div>
            <div className="homeContainer" style={{padding: "100px", marginBottom: "0px"}}>
                <form>
                    <input type="text" placeholder="Username" style={{fontSize: "32px"}}></input>
                    <br />
                    <input type="password" placeholder="Password" style={{fontSize: "32px"}}></input>
                </form>
            </div>
            <div style={{textAlign: "center"}}>
                <button className="navBarButton">Forgotten Password?</button>
                <div className="horizontalDivider"/>
                <Link to="/patientsearch">
                    <button className="navBarButton">Login</button>
                </Link>
            </div>
        </div>
    )
}

export default Login;