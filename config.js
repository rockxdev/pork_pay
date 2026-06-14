// ============================================================
//  Pork Pay — your settings live here.
// ============================================================

const PORK_PAY_CONFIG = {
  // Your Jupiter referral account (collects your fees). Verified on-chain.
  referralAccount: "3uvG6RFTyYYyFELvHoMNdQGHs3uYHtb7TXnCHSy8GG4s",

  // Your fee in basis points. 50 = 0.5%, 100 = 1%.
  referralFeeBps: 50,

  // Default the swap box to: pay with SOL, receive PORK (nudge people to buy PORK).
  defaultInputMint: "So11111111111111111111111111111111111111112", // SOL
  defaultOutputMint: "73jj6SFe9FKn6qqpaGwbSd7TL1sHheh3HqDo9RwA7BHB", // PORK
};
