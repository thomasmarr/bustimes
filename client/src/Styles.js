import styled, { createGlobalStyle } from 'styled-components'

export const Global = createGlobalStyle`
    body {
        background-color: ${props => props.theme.bgColor};
    }
`

export const ContentWrapper = styled.div`
    max-width:650px;
    margin:auto;
    color: ${props => props.theme.primaryFontColor};
    font-size: large;
    line-height: 2;
    padding:10px;
`

export const ThemeButton = styled.button`
    &&& {
        background-color: ${props => props.theme.themeBtnColor};
    }
    position: fixed;
    bottom: 15px;
    right: 15px;
    border-radius: 50%;
    height: 50px;
    width: 50px;
    line-height: 0.9;
`
