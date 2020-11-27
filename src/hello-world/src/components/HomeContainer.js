import React from 'react';
import NavBar from './NavBar';
import Demographics from './Demographics';

function HomeContainer() {
    return (
        <div className="homeContainer">
            <Demographics />
            <NavBar />
        </div>
    );
}

export default HomeContainer;