import React from 'react';
import renderer from 'react-test-renderer';

import { Items } from './Items';

describe("snapshot tests for a simple react program", () => {
    it('renders correctly where there are no items', () => {
        const tree = renderer.create(<Items />).toJSON();
        expect(tree).toMatchSnapshot();
    });
    
    it('renders correctly where there is a single item', () => {
        const items = ['one'];
        const tree = renderer.create(<Items items={items} />).toJSON();
        expect(tree).toMatchSnapshot();
    })
    
    it('renders correctly where there are multiple items', () => {
        const items = ['one', 'two', 'three'];
        const tree = renderer.create(<Items items={items} />).toJSON();
        expect(tree).toMatchSnapshot();
    })
})