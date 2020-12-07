import React from 'react';
import { Link, useHistory, useParams } from 'react-router-dom';

function NavBar(props) {
    let history = useHistory();
    let {num} = useParams();

    function handleChange(event) {
        history.push(`/patient/${num}/reqform/${event.target.value}`)
    }
    return (
        <div className="navBar">
            <Link to={`/patient/${num}/newnote`}>
                <button className="navBarButton" onClick={props.onClick}>
                    New Note
                </button>
            </Link>
            <select className="navBarButton" onChange={handleChange}>
                <option selected disabled>Requisition Forms</option>
                <option value="bloodwork">Blood Work</option>
                <option value="imaging">Imaging</option>
                <option value="ecg">ECG</option>
            </select>

            <Link to={`/patient/${num}/MDsearch`}>
                <button className="navBarButton" onClick={props.onClick}>
                    MD Search
                </button>
            </Link>
            <Link to={`/patient/${num}/prescription`}>
                <button className="navBarButton" onClick={props.onClick}>
                    Prescription
                </button>
            </Link>
            <div className="horizontalDivider" style={{width: "50%"}}/>
            <Link to='/'>
                <button className="navBarButton" onClick={props.onClick}>
                    Logout
                </button>
            </Link>
        </div>
    )
}

export default NavBar;