import React from 'react';
import { Link } from 'react-router-dom';

function Login(props) {
    return (
            <div>
                <div style={{textAlign: "right", marginRight: "50px"}}>
                    <button>Logout</button>
                </div>
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
                <button className="navBarButton" style={{marginRight: "100px"}}>Forgotten Password?</button>
                <Link to="/">
                    <button className="navBarButton">Login</button>
                </Link>
            </div>
        </div>
    )
}

// class Login extends React.Component {
//     constructor() {
//         super();
//         this.state={}
//     }

//     render() {
//         return (
//             <div>
//             <div style={{textAlign: "right", marginRight: "50px"}}>
//                 <button>Logout</button>
//             </div>
//                 <LoginPanel />
//             </div>
//         )
//     }
// }

// class LoginPanel extends React.Component {
//     constructor() {
//         super();
//         this.state={}
//     }
//     render() {
//         return (
//             <div>
//                 <div className="homeContainer" style={{padding: "100px", marginBottom: "0px"}}>
//                     <form>
//                         <input type="text" placeholder="Username" style={{fontSize: "32px"}}></input>
//                         <br />
//                         <input type="text" placeholder="Password" style={{fontSize: "32px"}}></input>
//                     </form>
//                 </div>
//                 <div style={{textAlign: "center"}}>
//                     <button className="navBarButton" style={{marginRight: "100px"}}>Forgotten Password?</button>
//                     <Link to="/">
//                         <button className="navBarButton">Login</button>
//                     </Link>
//                 </div>
//             </div>
//         )
//     }
// }

export default Login;