`use strict`;

describe('Get users via API', () => {

    it("Test GET empty users", () => {
        cy.request("/users")
            .then((response) => {
            expect(response.status).eq(200);
            expect(response.body).to.be.empty;
        })
    })
});