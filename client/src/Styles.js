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