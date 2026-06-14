# Facebook Caption — Agent Growth Protocol v0.3

## GPT-5.5 Review: 6.8/10

### Issues found:
- Hook too soft
- Too many internal jargon terms
- CTA weak
- Reads like a product pitch

### Improved version (GPT-5.5 rewrite):

---

AI agent hay bị lặp lại lỗi cũ?

Mình gặp đúng vấn đề này khi làm việc với Hermes và các agent khác: nếu nhét hết note thô, fix tạm, hay workflow chưa kiểm chứng vào memory thì bộ nhớ sẽ rất nhanh bị loãng và đầy rác.

Vì vậy mình làm **Agent Growth Protocol v0.3** — một cách để agent tự ghi lại kinh nghiệm theo hướng gọn, có kiểm chứng, và dùng lại được.

Cụ thể:
- Lưu lỗi, cách fix, và workflow mới vào **JSONL** như một nguồn ghi nhận chính.
- Chỉ khi được **kiểm tra lại** thì mới nâng lên thành rule trong config của agent.
- Đồng bộ những bài học đã verify vào **long-term memory**.
- Có tài liệu hỗ trợ **song ngữ Anh–Việt**.

Hiện tại phần auto-capture vẫn chưa hoàn toàn native, nên vẫn cần script hoặc cron hỗ trợ. Nhưng mình muốn hướng tới kiểu **automation thực tế**, không hype.

Repo ở đây, anh em nào đang làm AI agent thì xem thử và góp ý giúp mình nhé:
https://github.com/roverdude24/agent-growth-protocol
